# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 384
- HTTP: 95 alive / 65 gold
- HTTPS: 37 alive / 16 gold
- SOCKS4: 171 alive / 154 gold
- SOCKS5: 173 alive / 149 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48188
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
