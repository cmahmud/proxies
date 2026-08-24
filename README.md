# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 392
- HTTP: 123 alive / 58 gold
- HTTPS: 48 alive / 12 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 199 alive / 164 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33373
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
