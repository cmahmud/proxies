# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 400
- HTTP: 97 alive / 60 gold
- HTTPS: 184 alive / 14 gold
- SOCKS4: 177 alive / 157 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40653
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
