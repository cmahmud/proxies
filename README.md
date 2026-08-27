# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 422
- HTTP: 107 alive / 73 gold
- HTTPS: 112 alive / 26 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 173 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41796
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
