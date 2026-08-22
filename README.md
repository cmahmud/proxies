# SyndProxy private pool

## Current pool

- Alive now: 912
- Gold now: 398
- HTTP: 281 alive / 96 gold
- HTTPS: 182 alive / 31 gold
- SOCKS4: 229 alive / 141 gold
- SOCKS5: 220 alive / 130 gold

## Historical pool

- Discovered: 163255
- Ever alive: 31771
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
