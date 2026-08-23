# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 377
- HTTP: 84 alive / 55 gold
- HTTPS: 38 alive / 10 gold
- SOCKS4: 173 alive / 155 gold
- SOCKS5: 175 alive / 157 gold

## Historical pool

- Discovered: 174823
- Ever alive: 33103
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
