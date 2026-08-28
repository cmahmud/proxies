# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 437
- HTTP: 109 alive / 84 gold
- HTTPS: 144 alive / 22 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 191 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42333
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
