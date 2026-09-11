# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 343
- HTTP: 208 alive / 80 gold
- HTTPS: 128 alive / 39 gold
- SOCKS4: 53 alive / 52 gold
- SOCKS5: 241 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48516
- Ever gold: 1543

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
