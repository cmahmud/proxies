# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 380
- HTTP: 112 alive / 46 gold
- HTTPS: 44 alive / 10 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 179 alive / 164 gold

## Historical pool

- Discovered: 180671
- Ever alive: 33579
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
