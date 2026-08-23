# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 380
- HTTP: 88 alive / 58 gold
- HTTPS: 55 alive / 11 gold
- SOCKS4: 166 alive / 154 gold
- SOCKS5: 184 alive / 157 gold

## Historical pool

- Discovered: 174830
- Ever alive: 33117
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
