# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 400
- HTTP: 91 alive / 67 gold
- HTTPS: 45 alive / 17 gold
- SOCKS4: 172 alive / 155 gold
- SOCKS5: 183 alive / 161 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48142
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
