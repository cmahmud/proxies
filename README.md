# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 390
- HTTP: 164 alive / 62 gold
- HTTPS: 53 alive / 15 gold
- SOCKS4: 171 alive / 154 gold
- SOCKS5: 188 alive / 159 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33137
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
