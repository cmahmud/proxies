# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 381
- HTTP: 103 alive / 62 gold
- HTTPS: 47 alive / 13 gold
- SOCKS4: 157 alive / 153 gold
- SOCKS5: 172 alive / 153 gold

## Historical pool

- Discovered: 176240
- Ever alive: 33202
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
