# SyndProxy validated proxy pool

## Current pool

- Alive now: 462
- Gold now: 374
- HTTP: 82 alive / 52 gold
- HTTPS: 46 alive / 11 gold
- SOCKS4: 161 alive / 154 gold
- SOCKS5: 173 alive / 157 gold

## Historical pool

- Discovered: 175389
- Ever alive: 33123
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
