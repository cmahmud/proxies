# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 417
- HTTP: 105 alive / 67 gold
- HTTPS: 109 alive / 21 gold
- SOCKS4: 175 alive / 164 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41453
- Ever gold: 1332

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
