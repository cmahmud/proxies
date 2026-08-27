# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 403
- HTTP: 97 alive / 62 gold
- HTTPS: 157 alive / 15 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 198 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41094
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
