# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 455
- HTTP: 125 alive / 91 gold
- HTTPS: 53 alive / 32 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 178 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49283
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
