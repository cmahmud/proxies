# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 430
- HTTP: 103 alive / 74 gold
- HTTPS: 41 alive / 20 gold
- SOCKS4: 177 alive / 164 gold
- SOCKS5: 186 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48997
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
