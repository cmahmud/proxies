# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 455
- HTTP: 123 alive / 95 gold
- HTTPS: 52 alive / 32 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49318
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
