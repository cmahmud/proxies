# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 391
- HTTP: 125 alive / 62 gold
- HTTPS: 30 alive / 10 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 189 alive / 164 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33436
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
