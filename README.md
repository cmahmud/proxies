# SyndProxy private pool

## Current pool

- Alive now: 840
- Gold now: 398
- HTTP: 253 alive / 91 gold
- HTTPS: 181 alive / 30 gold
- SOCKS4: 201 alive / 141 gold
- SOCKS5: 205 alive / 136 gold

## Historical pool

- Discovered: 162762
- Ever alive: 31612
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
