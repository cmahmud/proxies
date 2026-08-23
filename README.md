# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 382
- HTTP: 101 alive / 58 gold
- HTTPS: 46 alive / 10 gold
- SOCKS4: 181 alive / 154 gold
- SOCKS5: 199 alive / 160 gold

## Historical pool

- Discovered: 174830
- Ever alive: 33110
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
