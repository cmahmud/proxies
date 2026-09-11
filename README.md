# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 445
- HTTP: 123 alive / 87 gold
- HTTPS: 48 alive / 29 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49252
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
