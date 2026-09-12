# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 449
- HTTP: 122 alive / 94 gold
- HTTPS: 58 alive / 30 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 181 alive / 166 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49324
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
