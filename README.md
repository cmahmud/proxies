# SyndProxy validated proxy pool

## Current pool

- Alive now: 393
- Gold now: 295
- HTTP: 110 alive / 73 gold
- HTTPS: 46 alive / 20 gold
- SOCKS4: 79 alive / 66 gold
- SOCKS5: 158 alive / 136 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47871
- Ever gold: 1499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
