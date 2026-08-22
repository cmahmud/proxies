# SyndProxy private pool

## Current pool

- Alive now: 770
- Gold now: 409
- HTTP: 206 alive / 91 gold
- HTTPS: 165 alive / 25 gold
- SOCKS4: 183 alive / 137 gold
- SOCKS5: 216 alive / 156 gold

## Historical pool

- Discovered: 162444
- Ever alive: 31447
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
