# SyndProxy private pool

## Current pool

- Alive now: 1171
- Gold now: 444
- HTTP: 380 alive / 109 gold
- HTTPS: 322 alive / 32 gold
- SOCKS4: 214 alive / 152 gold
- SOCKS5: 255 alive / 151 gold

## Historical pool

- Discovered: 153725
- Ever alive: 28560
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
