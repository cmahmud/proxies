# SyndProxy private pool

## Current pool

- Alive now: 1196
- Gold now: 420
- HTTP: 400 alive / 86 gold
- HTTPS: 263 alive / 14 gold
- SOCKS4: 255 alive / 156 gold
- SOCKS5: 278 alive / 164 gold

## Historical pool

- Discovered: 131718
- Ever alive: 20716
- Ever gold: 874

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
