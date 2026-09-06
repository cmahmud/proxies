# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 398
- HTTP: 93 alive / 65 gold
- HTTPS: 43 alive / 17 gold
- SOCKS4: 172 alive / 155 gold
- SOCKS5: 184 alive / 161 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48142
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
