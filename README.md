# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 370
- HTTP: 90 alive / 59 gold
- HTTPS: 70 alive / 11 gold
- SOCKS4: 167 alive / 154 gold
- SOCKS5: 171 alive / 146 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43432
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
