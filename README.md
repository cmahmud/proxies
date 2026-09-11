# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 433
- HTTP: 103 alive / 74 gold
- HTTPS: 57 alive / 27 gold
- SOCKS4: 187 alive / 164 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49132
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
