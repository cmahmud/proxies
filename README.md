# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 401
- HTTP: 94 alive / 64 gold
- HTTPS: 32 alive / 20 gold
- SOCKS4: 164 alive / 145 gold
- SOCKS5: 193 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48785
- Ever gold: 1566

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
