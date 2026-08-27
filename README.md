# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 422
- HTTP: 99 alive / 74 gold
- HTTPS: 113 alive / 25 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 172 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41791
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
