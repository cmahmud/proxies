# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 450
- HTTP: 123 alive / 80 gold
- HTTPS: 111 alive / 34 gold
- SOCKS4: 178 alive / 164 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45630
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
