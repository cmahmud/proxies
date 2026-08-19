# SyndProxy private pool

## Current pool

- Alive now: 1255
- Gold now: 512
- HTTP: 456 alive / 181 gold
- HTTPS: 359 alive / 48 gold
- SOCKS4: 196 alive / 123 gold
- SOCKS5: 244 alive / 160 gold

## Historical pool

- Discovered: 125667
- Ever alive: 19647
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
