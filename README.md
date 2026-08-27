# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 405
- HTTP: 104 alive / 61 gold
- HTTPS: 164 alive / 17 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 194 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40724
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
