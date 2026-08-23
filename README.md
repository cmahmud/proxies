# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 378
- HTTP: 101 alive / 60 gold
- HTTPS: 32 alive / 10 gold
- SOCKS4: 160 alive / 153 gold
- SOCKS5: 171 alive / 155 gold

## Historical pool

- Discovered: 174309
- Ever alive: 33084
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
