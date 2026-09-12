# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 435
- HTTP: 111 alive / 86 gold
- HTTPS: 51 alive / 28 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49428
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
