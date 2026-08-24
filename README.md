# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 392
- HTTP: 100 alive / 53 gold
- HTTPS: 51 alive / 15 gold
- SOCKS4: 164 alive / 158 gold
- SOCKS5: 192 alive / 166 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33398
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
