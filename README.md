# SyndProxy private pool

## Current pool

- Alive now: 830
- Gold now: 372
- HTTP: 227 alive / 68 gold
- HTTPS: 186 alive / 19 gold
- SOCKS4: 209 alive / 147 gold
- SOCKS5: 208 alive / 138 gold

## Historical pool

- Discovered: 148334
- Ever alive: 26163
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
