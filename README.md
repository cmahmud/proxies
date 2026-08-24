# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 384
- HTTP: 98 alive / 47 gold
- HTTPS: 61 alive / 14 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 186 alive / 164 gold

## Historical pool

- Discovered: 180329
- Ever alive: 33570
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
