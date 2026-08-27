# SyndProxy validated proxy pool

## Current pool

- Alive now: 610
- Gold now: 404
- HTTP: 93 alive / 61 gold
- HTTPS: 167 alive / 15 gold
- SOCKS4: 169 alive / 163 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41018
- Ever gold: 1316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
