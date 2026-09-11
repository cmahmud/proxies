# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 442
- HTTP: 124 alive / 86 gold
- HTTPS: 49 alive / 26 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49268
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
