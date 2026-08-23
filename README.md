# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 377
- HTTP: 84 alive / 53 gold
- HTTPS: 49 alive / 11 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 174 alive / 158 gold

## Historical pool

- Discovered: 175389
- Ever alive: 33123
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
