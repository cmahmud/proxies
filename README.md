# SyndProxy private pool

## Current pool

- Alive now: 813
- Gold now: 393
- HTTP: 216 alive / 88 gold
- HTTPS: 153 alive / 26 gold
- SOCKS4: 214 alive / 144 gold
- SOCKS5: 230 alive / 135 gold

## Historical pool

- Discovered: 163276
- Ever alive: 31796
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
