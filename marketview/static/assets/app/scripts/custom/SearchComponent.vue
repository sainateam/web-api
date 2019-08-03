<template>
		<div id="k_offcanvas_toolbar_search" class="k-offcanvas-panel">
			<div class="k-offcanvas-panel__head">
				<h3 class="k-offcanvas-panel__title">
					جست‌و‌جو
				</h3>
				<a href="#" class="k-offcanvas-panel__close" id="k_offcanvas_toolbar_search_close"><i class="flaticon2-delete"></i></a>
			</div>
			<div class="k-offcanvas-panel__body">
				<div class="k-search">
					<div class="k-search__form">
						<form action="#" method="get">
							<input type="text" name="query" class="form-control" placeholder="تایپ کنید...">
						</form>
					</div>
					<div class="k-search__result">
						<div class="k-search__section">
							سهام
						</div>
						<div class="k-search__item">
							<div class="k-search__item-img k-search__item-img--file">
								<img src="../assets/media/files/doc.svg" alt="" />
							</div>
							<div class="k-search__item-wrapper">
								<a href="#" class="k-search__item-title">
									AirPlus Requirements
								</a>
								<div class="k-search__item-desc">
									by Grog John
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

</template>

<script>
'use strict';

module.exports = {
	name: 'SearchComponent',
	data: function () {
		return {
			test: 'hi'
		}
	}
}
</script>

<style scoped>

</style>