# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 389
- HTTP: 126 alive / 63 gold
- HTTPS: 84 alive / 14 gold
- SOCKS4: 175 alive / 154 gold
- SOCKS5: 189 alive / 158 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33137
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
