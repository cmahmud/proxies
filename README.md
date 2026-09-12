# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 454
- HTTP: 123 alive / 95 gold
- HTTPS: 54 alive / 32 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49320
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
