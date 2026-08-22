# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 387
- HTTP: 336 alive / 77 gold
- HTTPS: 226 alive / 22 gold
- SOCKS4: 225 alive / 125 gold
- SOCKS5: 240 alive / 163 gold

## Historical pool

- Discovered: 164969
- Ever alive: 32247
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
