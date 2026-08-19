# SyndProxy private pool

## Current pool

- Alive now: 1009
- Gold now: 362
- HTTP: 283 alive / 61 gold
- HTTPS: 240 alive / 13 gold
- SOCKS4: 242 alive / 141 gold
- SOCKS5: 244 alive / 147 gold

## Historical pool

- Discovered: 129286
- Ever alive: 20267
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
