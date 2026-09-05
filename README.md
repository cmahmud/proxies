# SyndProxy validated proxy pool

## Current pool

- Alive now: 389
- Gold now: 299
- HTTP: 111 alive / 74 gold
- HTTPS: 45 alive / 22 gold
- SOCKS4: 79 alive / 66 gold
- SOCKS5: 154 alive / 137 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47872
- Ever gold: 1499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
