# SyndProxy private pool

## Current pool

- Alive now: 931
- Gold now: 347
- HTTP: 303 alive / 68 gold
- HTTPS: 192 alive / 15 gold
- SOCKS4: 227 alive / 141 gold
- SOCKS5: 209 alive / 123 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15282
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
