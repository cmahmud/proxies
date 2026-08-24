# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 385
- HTTP: 92 alive / 47 gold
- HTTPS: 57 alive / 14 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 187 alive / 164 gold

## Historical pool

- Discovered: 180329
- Ever alive: 33569
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
